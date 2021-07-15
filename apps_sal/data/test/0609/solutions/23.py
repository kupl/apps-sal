def solve(arr, n):
    symbol = arr[0][0]
    for i in range(0,n):
        if arr[i][i] != symbol:
            return 'NO'
    j=0
    for i in range(n-1,-1,-1):
        if arr[i][j] != symbol:
            return 'NO'
        j+=1
    return 'YES'


n = int(input())

chars = []
while len(chars) < n:    
    s = input()
    chars.append(list(s))

L = sum(chars,[])
amount = set(sum(chars,[]))

if len(amount) == 2 and L.count(L[0]) == n*2-1:
    print(solve(chars, n))
else:
    print('NO')
