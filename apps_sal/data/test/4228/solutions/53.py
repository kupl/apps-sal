n,l = map(int,input().split())

lt = [l+i for i in range(n)]

if(min(lt) > 0):
    print(sum(lt[1:]))
elif(max(lt) < 0):
    print(sum(lt[:n-1]))
else:
    print(sum(lt))
