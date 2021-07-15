from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

h,w,m=nii()

hl=[0 for i in range(h+1)]
wl=[0 for i in range(w+1)]
hwl=set()

for i in range(m):
  th,tw=nii()
  hl[th]+=1
  wl[tw]+=1
  hwl.add((th,tw))

h_max=max(hl)
w_max=max(wl)

h_cand=[i for i in range(h+1) if hl[i]==h_max]
w_cand=[i for i in range(w+1) if wl[i]==w_max]

for i in h_cand:
  for j in w_cand:
    if (i,j) not in hwl:
      print(h_max+w_max)
      return

print(h_max+w_max-1)
