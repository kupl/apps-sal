K = int(input())
(A, B) = map(int, input().split())
'\nif(B-A+1 >= K):\n  print("OK")\nelse:\n  print("NG")\n'
flag = False
for i in range(A, B + 1):
    if i % K == 0:
        flag = True
if flag:
    print('OK')
else:
    print('NG')
