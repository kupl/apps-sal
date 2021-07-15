n = int(input())
s = list(map(str, input().split()))
for i in s:
    if i == 'Y':
        print('Four')
        break

# 4種類か3種類かは、黄色Yが入ってるかどうか

else:
    print('Three')
