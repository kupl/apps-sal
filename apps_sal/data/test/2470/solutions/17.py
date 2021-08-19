class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # TC: O(min(M, N)*N+MlogM), SC: O(min(M, N))
        m, n = len(arr1), len(arr2)
        # sort O(MlogM)
        arr2.sort()
        # maintain a list of (num-of-swaps, last-value, next-to-swap-index-arr2),
        # where the last value should be decrease as the num of swaps is increase
        ss = [(0, arr1[0], 0)]
        if arr2[0] < arr1[0]:
            ss.append((1, arr2[0], 1))
        # O(N) iteration
        for i in range(1, m):
            st = []
            # O(min(M, N))
            for s, x, j in ss:
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
                # amortized O(1)
                while j < n and arr2[j] <= x:
                    j += 1
                if j < n:
                    st.append((s + 1, arr2[j], j))
            # since each swap takes at most 1 entry, and at most O(min(M, N)) swap, so SC: O(min(M, N))
            ss = st
        return ss[0][0] if ss else -1
