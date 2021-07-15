from typing import List
from collections import Counter
class Solution:
  def numTriplets(self, en1: List[int], en2: List[int]) -> int:




    counter1=Counter(en1)
    counter2=Counter(en2)

  
    ct = 0
    for ele1,ct1 in list(counter1.items()):
      tot = ele1*ele1
      for ele2 in counter2:
        div,mod = divmod(tot,ele2)
        if mod !=0: continue
        if div in counter2:
          if ele2 == div:
            ct+=ct1*counter2[ele2]*(counter2[div]-1)
          else:
            ct+=ct1*counter2[ele2]*counter2[div]
            
    for ele1,ct1 in list(counter2.items()):
      tot = ele1*ele1
      for ele2 in counter1:
        div,mod = divmod(tot,ele2)
        if mod !=0: continue
        if div in counter1:
          if ele2 == div:
            ct+=ct1*counter1[ele2]*(counter1[div]-1)
          else:
            ct+=ct1*counter1[ele2]*counter1[div]

    return ct//2

