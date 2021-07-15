l = list(range(2,14))+[1]
a,b = list(map(int,input().split()))
a,b = l.index(a),l.index(b)
print(("Draw" if a == b else "Alice" if a > b else "Bob"))

