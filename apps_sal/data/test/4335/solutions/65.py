#入力を受け取る
N=int(input())
S=input()

result='No'

#長さが奇数か偶数か判断する
#奇数であれば'No'、偶数であれば半分に割った文字列をそれぞれを比較して一致していれば'Yes'
if len(S)%2==0:
     if S[:len(S)//2]==S[len(S)//2:]:
            result='Yes'

#出力する
print(result)
