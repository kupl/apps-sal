class Solution:

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        (m, n) = (len(arr1), len(arr2))
        arr2.sort()
        ss = [(0, arr1[0], 0)]
        if arr2[0] < arr1[0]:
            ss.append((1, arr2[0], 1))
        for i in range(1, m):
            st = []
            for (s, x, j) in ss:
                if x < arr1[i]:
                    if st:
                        if s == st[-1][0]:
                            if arr1[i] < st[-1][1]:
                                st[-1] = (s, arr1[i], j)
                        elif s > st[-1][0]:
                            if arr1[i] < st[-1][1]:
                                st.append((s, arr1[i], j))
                    else:
                        st.append((s, arr1[i], j))
                while j < n and arr2[j] <= x:
                    j += 1
                if j < n:
                    st.append((s + 1, arr2[j], j))
            ss = st
        return ss[0][0] if ss else -1
