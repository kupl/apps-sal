class Solution(object):
    def shortestSubarray(self, A, K):
        n = len(A)
        pref = [0]*(n+1)
        for i in range(1, n+1):
            pref[i] = pref[i-1] + A[i-1]
        
        node = deque(); ans = n + 1
        for i in range(len(pref)):
            while node and pref[i] - pref[node[0]] >= K:
                ans = min(ans, i-node[0])
                node.popleft()
            while node and pref[i] <= pref[node[-1]]:
                node.pop()
            node.append(i)
        
        return ans if ans < n+1 else -1

