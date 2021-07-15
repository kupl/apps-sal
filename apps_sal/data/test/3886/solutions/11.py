s0 = 'What are you doing at the end of the world? Are you busy? Will you save us?'
s1 = 'What are you doing while sending "'
s2 = '"? Are you busy? Will you send "'
def get(h): 
    if h > 55: return 1<<99
    return (143 << h) - 68
def solve(n, k):
    if get(n) <= k: return '.'
    while True:
        if n == 0: return s0[k]
        if k < 34: return s1[k]
        k -= 34
        if k < get(n-1): 
          n -= 1
          continue
        k -= get(n-1)
        if k < 32: return s2[k]
        k -= 32
        if k < get(n-1): n -=1
        else: return '"?'[k - get(n - 1)]
for i in range(int(input())):
    n,k=list(map(int,input().split()))
    print(solve(n,k-1),end='')
    
