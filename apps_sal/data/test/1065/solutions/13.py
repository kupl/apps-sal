import math
[n, k, M, D] = input().split()
n = int(n)
k = int(k)
M = int(M)
D = int(D)
'\nll best=0;\n\tfor (ll i=0; i<=(D-1); i++){\n\t\tll x=min(up,n/(i*k+1));\n\t\tll score=(i+1)*x;\n\t\tbest=max(best,score);\n\t}\n\t\n\tcout<<best<<endl;\n'
best = 0
for i in range(D):
    x = min(M, n // (i * k + 1))
    score = (i + 1) * x
    best = max(best, score)
print(best)
