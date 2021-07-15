n, k, p, x, y=map(int, input().split())
s=list(map(int, input().split()))
s=sorted(s)
if p<y:
    print(-1)
else: 
    kol=0
    summ=0
    for i in s: #������� ����� � ���������� ������� ��� y
        summ+=i
        if i>=y:
            kol+=1
    if k-kol>=n//2+1 or summ > x: #���� ������� �������� ������ y
        print(-1)#, '!1')
    elif kol>=n//2+1: #���� ������� �������� ������ y
        if summ+n-k <=x:
            print('1 '*(n-k))
        else:
            print(-1)#, '!2')
    else: #���������� � ������� �����
        #print('!!!', summ, y*(n//2+1-kol), n-k-n//2-1+kol, kol)
        if summ+y*(n//2+1-kol)+(n-k-n//2-1+kol)>x:
            print(-1)#, '!3')
        else:
            for i in range(n//2+1-kol):
                print(y, end=' ')
            for i in range(n-k-n//2-1+kol):
                print('1', end = ' ')
            
