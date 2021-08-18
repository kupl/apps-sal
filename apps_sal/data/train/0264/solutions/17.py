class Solution:
    from collections import Counter

    def maxLength(self, arr: List[str]) -> int:
        st = [(None, 0)]
        l = 0
        ind_dic = {}
        new_ind = 0
        for i in range(len(arr)):
            ind_dic[i] = Counter(arr[i])
        while st:
            sub, ind = st.pop(0)
            if sub:
                l = max(l, len(sub))
            if ind >= len(arr):
                continue
            if not sub:
                st.append((None, ind + 1))
                if len(arr[ind]) == len(set(arr[ind])):
                    st.append((arr[ind], ind + 1))
            else:
                cur_dic = Counter(sub)
                if set(cur_dic.keys()).intersection(set(ind_dic[ind].keys())):
                    st.append((sub, ind + 1))
                elif len(arr[ind]) > len(set(arr[ind])):
                    st.append((sub, ind + 1))
                else:
                    st.append((sub + arr[ind], ind + 1))
                    st.append((sub, ind + 1))
            new_ind = ind

        return l
