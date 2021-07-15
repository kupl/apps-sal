class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        dic = {}
        endpoints = {}
        startpoints = {}
        latest = -1
        for i in range(len(arr)):
            step = arr[i]
            if step-1 in endpoints:
                if step+1 not in startpoints:
                    j = endpoints[step-1]
                    startpoints[j] = step
                    endpoints[step] = j
                    del endpoints[step-1]
                    l = step-j
                    dic[l] -= 1
                    if l+1 in dic:
                        dic[l+1] += 1
                    else: dic[l+1] = 1
                else:
                    j = endpoints[step-1]
                    k = startpoints[step+1]
                    startpoints[j] = k
                    endpoints[k] = j
                    del startpoints[step+1]
                    del endpoints[step-1]
                    l1 = step-j
                    l2 = k-step
                    dic[l1] -= 1
                    dic[l2] -= 1
                    if l1+l2+1 in dic:
                        dic[l1+l2+1] += 1
                    else: dic[l1+l2+1] = 1
            elif step+1 in startpoints:
                k = startpoints[step+1]
                endpoints[k] = step
                startpoints[step] = k
                del startpoints[step+1]
                l = k-step
                dic[l] -= 1
                if l+1 in dic:
                    dic[l+1] += 1
                else: dic[l+1] = 1
            else:
                endpoints[step] = step
                startpoints[step] = step
                if 1 in dic:
                    dic[1] += 1
                else: dic[1] = 1
            if m in dic and dic[m]!=0:
                latest = i+1
        return latest

