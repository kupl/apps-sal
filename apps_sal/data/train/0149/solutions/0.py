class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st=[['*',0]]
        for c in s:
            if c!=st[-1][0]:
                st.append([c,1])
            else:
                st[-1][1]+=1
                if st[-1][1]==k:
                    st.pop()
        res=''
        for c,v in st:
            res+=c*v
        return res
