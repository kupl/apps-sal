class Solution:
  def hasAllCodes(self, s: str, k: int) -> bool:
      need = 1 << k # Equivalent to 2^k
      got = set()

      for i in range(k, len(s)+1):
        tmp = s[i-k:i]
        if tmp not in got:
          got.add(tmp)
          need -= 1

          if need == 0: # Found everything
            return True
      return False

