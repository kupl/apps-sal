# 整数A,Bがあります。A+B,A−B,A×Bの中で最大の数を出力してください。

A,B = map(int,input().split())

print(max(A+B, A-B, A*B))
