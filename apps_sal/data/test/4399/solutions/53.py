# 駅１、２、３
# 管理状況はAAB,ABA、BBA,BBBなど、長さ３の文字列で表される
# AとBの駅の間にはバスを運行することにした
# バスが運行することになる組み合わせが存在するかどうか判定し、yes,noで出力
s = input('')
if s == 'AAA' or s == 'BBB':
    print('No')
else:
    print('Yes')
