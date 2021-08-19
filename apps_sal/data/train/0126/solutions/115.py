class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        i = numUnique = 0
        N = len(s)
        count = collections.defaultdict(int)
        seen = collections.defaultdict(int)
        ans = 0

        for i in range(N):
            count = collections.defaultdict(int)
            numUnique = 0
            power = 1
            hash = 0
            for j in range(i, min(i + 26, N)):
                count[s[j]] += 1
                if count[s[j]] == 1:
                    numUnique += 1

                add = (ord(s[j]) - ord('a') + 1) * (27**power)
                hash += add
                power += 1

                if numUnique > maxLetters or j - i + 1 > maxSize:
                    break

                if minSize <= j - i + 1 <= maxSize and numUnique <= maxLetters:
                    # have a valid subs
                    # print(s[i:j+1], hash)
                    seen[hash] += 1
                    ans = max(ans, seen[hash])

        return ans

        # for j in range(N):


#         for j in range(N):
#             if count[s[j]]==0:
#                 numUnique+=1

#             count[s[j]]+=1

#             while j-i+1>maxSize or numUnique>maxLetters:
#                 count[s[i]]-=1
#                 if count[s[i]]==0:
#                     numUnique-=1
#                 i+=1

#             if j-i+1>=minSize:
#                 # we finally have a valid substring
#                 for k in range(i,j+1):
#                     curr=\"\"
#                     for l in range(k,j+1):
#                         curr+=s[l]
#                         if len(curr)>=minSize:
#                             seen[curr]+1=26

#                 subs=s[i:j+1]
#                 seen[subs]+=1
#                 ans=max(ans,seen[subs])

#         print(seen)
#         return ans
