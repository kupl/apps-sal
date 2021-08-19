class Solution:
    def racecar(self, target: int) -> int:
        st = [(0, 1, '')]
        visited = set()

        while st:
            a = st.pop(0)
            if a[0] == target:
                return len(a[2])
            # put a 'A'
            if 0 <= a[0] + a[1] < 2 * target and (a[0] + a[1], a[1] * 2) not in visited:
                st.append((a[0] + a[1], a[1] * 2, a[2] + 'A'))
                visited.add((a[0] + a[1], a[1] * 2))

            # put a 'R'
            if a[0] >= 0 and (a[0], -1 if a[1] > 0 else 1) not in visited:
                st.append((a[0], -1 if a[1] > 0 else 1, a[2] + 'R'))
                visited.add((a[0], -1 if a[1] > 0 else 1))

        return -1
