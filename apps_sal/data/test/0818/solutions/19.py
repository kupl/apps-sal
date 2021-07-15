n = int(input());
ti = 1;

if(n<=2):
    print(-1);
    return;

n-=2;
ti = 10**n;

if(ti%21):
    ti//=21;
    ti+=1;
    ti*=21;
ti*=10;
print(ti);
