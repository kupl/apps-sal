import math

[n, k, M, D] = input().split()
n = int(n)
k = int(k)
M = int(M)
D = int(D)
"""
ll best=0;
	for (ll i=0; i<=(D-1); i++){
		ll x=min(up,n/(i*k+1));
		ll score=(i+1)*x;
		best=max(best,score);
	}
	
	cout<<best<<endl;
"""
best = 0
for i in range(D):
    x = min(M, (n // (i * k + 1)))
    score = (i + 1) * x
    best = max(best, score)
print(best)
