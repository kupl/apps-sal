s=0;
q=0;
n = int(input());
qq=0;
w = str(input());
w1=w.split()

while qq<n:
    qwe=int(w1[qq]);
    if (qwe%2==0):
        s=s+1;
    else:
        q=q+1
    qq = qq + 1;

if q<=s:
    print(q);
else:
    print(s+(q-s)//3)
