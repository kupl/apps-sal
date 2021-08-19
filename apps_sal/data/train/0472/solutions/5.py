class Solution:

    def canReach(self, jumps: List[int], start: int) -> bool:
        st = [start]
        size = len(jumps)
        while st:
            idx = st.pop()
            jump = jumps[idx]
            if jump < 0:
                continue
            (left, right) = (idx - jump, idx + jump)
            for i in [left, right]:
                if 0 <= i < size:
                    if jumps[i] == 0:
                        return True
                    st.append(i)
            jumps[idx] = -1
        return False
