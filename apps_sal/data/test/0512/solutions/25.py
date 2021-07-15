
def main(): 
    n = int(input())
    
    #各階の乗降客の情報
    arr = [[0,0] for i in range(2*n+1)]
    
    for i in range(n):
        a,b = map(int,input().split())
        #乗った階層の情報が与えられていない
        #The 
        if a==-1:
            pass
        #別の乗客がその階層で乗降していない
        elif arr[a]==[0,0]:
            arr[a] = [i+1,b]
        #別の乗客がその階層で乗降しているので、問題条件を満たさない
        else:
            arr[a] = [2**16,2**16]
        if b==-1:
            pass
        elif arr[b]==[0,0]:
            arr[b] = [-i-1,a]
        else:
            arr[b] = [2**16,2**16]
            
    #2i階まで条件を満たす階層の組み合わせがあるかを記憶
    ans = [False for i in range(n+1)]
    ans[0] = True

    #lo階からhi階までについて考える
    for hi in range(2,2*n+2,2):
        for lo in range(1,hi+1,2):
          
          	#lo-1階へたどり着く組み合わせがないのでスキップ
            if not ans[lo//2]:
                continue
                
            #lo階からhi階までについて、問題条件を満たしているか
            flag = True
            for i in range(lo,lo+(hi-lo+1)//2):
              
              	#x階で乗客が乗った場合、y階で降りれば条件を満たす
                x,y = arr[i],arr[i+(hi-lo+1)//2]

                #x階、y階共にまだ乗降する乗客が指定されていない
                if x==[0,0] and y==[0,0]:
                    continue
                    
                #x階のみ指定されていない
                elif x==[0,0]:
                  	#y階で客が乗っているか、y階で降りた客はx階以外の階層で乗っている
                    if y[0]>0 or y[1]!=-1:
                        flag = False
                        break
                        
                elif y==[0,0]:
                    if x[0]<0 or x[1]!=-1:
                        flag = False
                        break
                        
                #x階、y階共に乗客が指定されている
                else:
                  	#x階、y階で乗降した客が同じでないか、x階で降りてy階で乗っている
                    if x[0]!=-y[0] or x[0]<0:
                        flag = False
                        break
                    elif x[1]!=i+1+(hi-lo-1)//2 or y[1]!=i:
                        flag = False
                        break

            #lo階からhi階までの組み合わせが条件を満たしているか
            if not flag:
                continue
            ans[hi//2] = True

    if ans[-1]:
        print("Yes")
    else:
        print("No")


def __starting_point():
    main()
__starting_point()
