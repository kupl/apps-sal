class Solution:
     def lengthLongestPath(self, input):
         """
         :type input: str
         :rtype: int
         """
         dict={0:0}
         maxlen=0
         line=input.split("\n")
         for i in line:
             name=i.lstrip('\t')
             print(name)
             print((len(name)))
             depth=len(i)-len(name)
             if '.' in name:
                 maxlen=max(maxlen, dict[depth]+len(name))
             else:
                 dict[depth+1]=dict[depth]+len(name)+1
         return maxlen

