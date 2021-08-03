S = input()
mod = 2019

array = []
for i in range(len(S)):
    x = (int(S[len(S) - 1 - i]) * pow(10, i, mod)) % mod
    array.append(x)
array2 = [0]
y = 0
for i in range(len(S)):
    y = (y + array[i]) % mod
    array2.append(y)
array3 = [0] * 2019
ans = 0
for i in range(len(array2)):
    z = array2[i]
    ans += array3[z]
    array3[z] += 1
print(ans)
# 3*673
