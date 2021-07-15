# 4種類の塩基 A,C,G,T が存在し、 A と T 、 C と G がそれぞれ対
# A,C,T,G いずれかの文字 b が入力される
# 塩基 b と対になる塩基をあらわす文字を出力

b = input()

if b == 'A':
    print('T')
elif b == 'C':
    print('G')
elif b == 'G':
    print('C')
else:
    print('A')
