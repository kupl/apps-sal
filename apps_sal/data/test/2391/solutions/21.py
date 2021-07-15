num = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
d = []

for i in range(num):
    c.append(a[i] ^ a[(i+1)%num])
    d.append(b[i] ^ b[(i+1)%num])
    
c += c

# print(c)
# print(d)

# テーブル作成
table = [0]
k = 0
for i in range(1, num+1):
    table.append(k)
    if i == num:
        continue
    
    if d[i] == d[k]:
        k += 1
    else:
        k = 0

# print(table)

i = 0 # 探索される文字列の位置
j = 0 # 探索する文字列の位置
k = 0 # kの初期値
while k < num:
    
    while True:
        # print(i, j, k)
        if c[i] == d[j]:
            if j == num - 1:
                print(k, a[k] ^ b[0])
                i += 1
                j = table[num]
                k = i - j
                break
            
            i += 1
            j += 1
        elif j != 0:
            j -= 1
        else:    
            i += 1
            j = table[j]
            break
    
    k = i - j
