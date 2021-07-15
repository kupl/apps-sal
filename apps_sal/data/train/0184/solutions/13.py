class Solution:
    def maxRepOpt1(self, text: str) -> int:
        max_char=''
        clist=[1]*len(text)
        one_max=1
        compress_list=[]
        for i in range(1,len(text)):
            if text[i]==text[i-1]:
                clist[i]=clist[i-1]+1
            else:
                clist[i]=1
                compress_list.append([text[i-1],clist[i-1]])
            if clist[i]>one_max:
                one_max=clist[i]
                max_char=text[i]
        compress_list.append([text[-1],clist[-1]])
        print(compress_list)
        two_count=[]
        two_max=0
        for i in range(2,len(compress_list)):
            if compress_list[i-1][1]>1:
                continue
            if compress_list[i][0]!=compress_list[i-2][0]:
                continue
            if compress_list[i][1]+compress_list[i-2][1]+1<two_max:
                continue
            c=compress_list[i][0]
            swaped=False
            for j in range(len(compress_list)):
                if j>=i-2 and j<=i:
                    continue
                if compress_list[j][0]==c:
                    len2=compress_list[i][1]+compress_list[i-2][1]+1
                    two_count.append(len2)
                    if len2>two_max:
                        two_max=len2
                    swaped=True
            if swaped:
                continue
            len2 = compress_list[i][1] + compress_list[i - 2][1]
            two_count.append(len2)
            if len2 > two_max:
                two_max = len2
        if one_max>=two_max:
            char_count=0
            for i in range(len(compress_list)):
                if compress_list[i][0]==max_char:
                    char_count+=1
            if char_count>1:
                one_max+=1
        return max(one_max,two_max)
