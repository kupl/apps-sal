a,b,k=map(int, input().split())
ra=max(a-k,0)
if k>a:
    b=max(b-(k-a),0)
print(ra,b)
