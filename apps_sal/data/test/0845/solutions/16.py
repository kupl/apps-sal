ch=input()
st=input()
d0={'R':-1,'L':1}
st2='qwertyuiopasdfghjkl;zxcvbnm,./'
print(''.join([st2[st2.find(ch2)+d0[ch]] for ch2 in st]))
