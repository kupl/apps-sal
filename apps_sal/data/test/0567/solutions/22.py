n=int(input())
niz=list(map(int,input().split()))
poz1=1
poz2=10**6
vreme=0
for nagrada in niz:
    tr1=nagrada-poz1
    tr2=poz2-nagrada
    vreme=max(vreme,min(tr1,tr2))
print(vreme)
