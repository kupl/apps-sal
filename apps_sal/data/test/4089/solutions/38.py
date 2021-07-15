n = int(input())

ans = ''
# 制約条件は高々 26 の 10 乗なので、取り合えずインデックスを13に設定して回す
for i in range(1, 13):
    if n <= 26**i:
        n -= 1
        for j in range(i):
            ans += chr(ord('a') + n%26)
            n //= 26
        break;
    else:
        n -= 26**i

print(ans[::-1])
