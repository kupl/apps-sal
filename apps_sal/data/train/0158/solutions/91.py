class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        queue = []

        queue.append((A,B,0))  
        step = len(A)
        minFlip = float('inf')
        seen = {(A,B):0}
        while(queue):
            target, current, flip = queue.pop(0) 
            if seen[(target,current)] < flip:
                continue
            if target == current:
                minFlip = min(minFlip,flip)
                continue
            if target[0] == current[0]:
                temp = seen.get((target[1:], current[1:]), None)
                if not temp:
                    seen[(target[1:], current[1:])] = flip
                else:
                    if temp <= flip:
                        continue
                seen[(target[1:], current[1:])] = flip
                queue.append((target[1:], current[1:], flip))
            else:
                canni = [idx for idx, char in enumerate(current) if char == target[0]]
                piror = canni
                #piror = [(loc, target[loc] == current[0]) for loc in canni]
                #piror.sort(key=lambda x:x[1],reverse = True)
                for loc in piror:
                    lol = (target[1:], current[1:loc] + current[0] + current[loc+1:]) 
                    temp = seen.get(lol, None)
                    if not temp:
                        seen[lol] = flip+1
                    else:
                        if temp <= flip+1:
                            continue
                    seen[lol] = flip + 1
                    queue.append((target[1:], current[1:loc] + current[0] + current[loc+1:], flip + 1))

        return minFlip
            

