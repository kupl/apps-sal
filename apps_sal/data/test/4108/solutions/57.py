from collections import Counter
s = input()
t = input()
#文字の順番入れ替えは可能
#文字の個数は増やせない
#結局はaabbbなら2,3になる
#abcdbならa:1,b:2,c:1,d:1
s_dict = Counter(s)
t_dict = Counter(t)
s_val = list(s_dict.values())
t_val = list(t_dict.values())
s_val.sort()
t_val.sort()
if s_val == t_val:
    print('Yes')
else:
    print('No')


