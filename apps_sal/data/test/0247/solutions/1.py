n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    xi, yi = list(map(int, input().split()))
    x[i], y[i] = xi, yi

if n <= 4:
    print("YES"); return

l = lambda i, j, k : (y[i] - y[j]) * (x[i] - x[k]) == (y[i] - y[k]) * (x[i] - x[j])

def check(ind):
    if len(ind) <= 2:
        return True
    for k in range(2, len(ind)):
        if not l(ind[0], ind[1], ind[k]):
            return False
    return True

def diff(i, j):
    return [_ for _ in range(n) if not l(i, j, _)]
        
df = diff(0, 1)

if check(df):
    print("YES"); return
f = df[0]

df2 = diff(0, f)
if check(df2):
    print("YES"); return

df3 = diff(1, f)
if check(df3):
    print("YES"); return

print("NO")
        

    


