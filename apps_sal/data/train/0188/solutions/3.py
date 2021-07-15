class Solution:
     def numberToWords(self, num):
         """
         :type num: int
         :rtype: str
         """
         if num==0:
             return "Zero"
         res=""
         less20=["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
         tens=["Zero","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
         thousands=["","Thousand","Million","Billion"]
         for k in range(4):
             if num ==0:
                 break
             cur=""
             curNum=num%1000
             num//=1000
             print(("num",num))
             if curNum>=100:
                 x=curNum//100
                 curNum%=100
                 cur=less20[x]+" Hundred"
             if curNum>0:
                 if cur:
                     cur+=" "
                 if curNum<20:
                     cur+=less20[curNum]
                 else:
                     x=curNum//10
                     curNum%=10
                     cur+=tens[x]
                     if curNum!=0:
                         cur+=" "+less20[curNum]
             print("cur")
             if cur:
                 res=cur+((" "+thousands[k] if k else"")) +((" "+res if res else""))
         return res

