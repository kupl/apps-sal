n, k = map(int, input().split())
p = list(map(int, input().split()))


def count_invs(a):
    ans = 0
    for i in range(n-1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                ans += 1
    return ans
    

def inv_in_perms(a, count):
    if count > 0:
        ans = 0
        for l in range(n):
            for r in range(l, n):
                a[l: r + 1] = a[l: r + 1][::-1]        
                ans += inv_in_perms(a, count - 1)
                a[l: r + 1] = a[l: r + 1][::-1]   
        return(ans)
    else:
        return(count_invs(a))

                
total = (n * (n + 1) // 2) ** k
perms = 0

print(inv_in_perms(p, k) / total)        
