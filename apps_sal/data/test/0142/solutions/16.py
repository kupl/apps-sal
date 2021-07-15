def solve(a1,b1, cur_sum, cur_L, idx):
    if cur_L == 0:
        return cur_sum
    if idx == len(a1)-1:
        if cur_L > 0:
            ost = cur_L%b1[-1] > 0
            if ost:
                cur_sum += a1[-1]
            cur_sum += a1[-1]* (cur_L//b1[-1])
            return cur_sum
        else:
            return cur_sum
    else:
        ost = cur_L%b1[idx] > 0
        if ost:
            s1 = solve(a1,b1, cur_sum+a1[idx]*((cur_L//b[idx]) + 1), 0,idx+1)
            s2 = solve(a1,b1, cur_sum+a1[idx]*((cur_L//b[idx])), cur_L % b1[idx],idx+1)
            return min(s1,s2)
        else:
            return solve(a1,b1, cur_sum+a1[idx]*((cur_L//b[idx])), cur_L % b1[idx],idx+1)
            

            
n, L = list(map(int, input().split()))
a = list(map(int,input().split()))
b = [2**i for i in range(len(a))]
for i in range(len(a)):
        for j in range(len(a) - 1, i, -1):
            if a[j]/b[j] < a[j-1]/b[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                b[j], b[j-1] = b[j-1], b[j]
ans = solve(a,b,0,L,0)
print (ans)

        

