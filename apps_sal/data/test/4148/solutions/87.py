# 入力を受け取る
N=int(input())
S=input()

# 文字cをN文字ずらすことを考える（Aを基準とした26進数を考える）

# Aの文字コードを取得する
code_A = ord('A')

results = ''

for c in S:
    # 文字cをn文字シフトした文字コードを求める
    # 文字cをn文字シフトした文字コードから(Aで規格化するために)Aの文字コードを減算して26で割った余りを考える
    after_n = (ord(c)+N-code_A)%26
    
    # 結果を文字リストに追加していく
    results += chr(code_A+after_n)

# 出力する
print(results)
