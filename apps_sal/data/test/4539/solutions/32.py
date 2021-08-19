N = int(input())
x = str(N)
s = 0
for i in range(len(x)):
    s += int(x[i])
if N % s == 0:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
