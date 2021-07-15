A,B,K = map(int,input().split())


if A+B <= K:
    print('0 0')

elif A<K and K<A+B :
    print(0,A+B-K,sep=' ')

else: #K<A
    print(A-K,B,sep=' ')
