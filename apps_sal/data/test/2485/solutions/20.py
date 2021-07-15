h,w,m=map(int,input().split())

st=set()
h_b=[0 for i in range(h)]
w_b=[0 for i in range(w)]
for i in range(m):
  th,tw=map(int,input().split())
  th-=1
  tw-=1
  st.add((th,tw))
  h_b[th]+=1
  w_b[tw]+=1

h_max=max(h_b)
w_max=max(w_b)

h_cand=[i for i in range(h) if h_b[i]==h_max]
w_cand=[i for i in range(w) if w_b[i]==w_max]

for i in h_cand:
  for j in w_cand:
    if (i,j) not in st:
      print(h_max+w_max)
      return

print(h_max+w_max-1)
