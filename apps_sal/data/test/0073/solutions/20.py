c, v0, v1, a, l = list(map(int, input().split()))

v = v0;

read = v;
day = 1;
v += a
v = min(v, v1)


if(read >= c):
    print(day)
    return;


while(True):
    day +=1;
    read += v - l

    v+=a
    v = min(v, v1)
    if(read >= c):
        print(day)
        return;


