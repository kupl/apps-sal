# A - Buying Sweets

# X円で、A円のケーキ1個と、B円のドーナツを買えるだけ買った場合、残りは何円か


X = int(input())
A = int(input())
B = int(input())

print(((X - A) % B))
