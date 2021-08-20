s1 = input()
s2 = input()
s3 = input()
s4 = input()
s5 = s1[0] + s2[0] + s3[0] + s4[0]
s6 = s1[1] + s2[1] + s3[1] + s4[1]
s7 = s1[2] + s2[2] + s3[2] + s4[2]
s8 = s1[3] + s2[3] + s3[3] + s4[3]
s9 = s2[0] + s3[1] + s4[2]
s10 = s1[0] + s2[1] + s3[2] + s4[3]
s11 = s1[1] + s2[2] + s3[3]
s12 = s1[2] + s2[1] + s3[0]
s13 = s1[3] + s2[2] + s3[1] + s4[0]
s14 = s2[3] + s3[2] + s4[1]
f = False
if 'xx.' in s1 or 'xx.' in s2 or 'xx.' in s3 or ('xx.' in s4) or ('xx.' in s5) or ('xx.' in s6) or ('xx.' in s7) or ('xx.' in s8) or ('xx.' in s9) or ('xx.' in s10) or ('xx.' in s11) or ('xx.' in s12) or ('xx.' in s13) or ('xx.' in s14):
    f = True
if 'x.x' in s1 or 'x.x' in s2 or 'x.x' in s3 or ('x.x' in s4) or ('x.x' in s5) or ('x.x' in s6) or ('x.x' in s7) or ('x.x' in s8) or ('x.x' in s9) or ('x.x' in s10) or ('x.x' in s11) or ('x.x' in s12) or ('x.x' in s13) or ('x.x' in s14):
    f = True
if '.xx' in s1 or '.xx' in s2 or '.xx' in s3 or ('.xx' in s4) or ('.xx' in s5) or ('.xx' in s6) or ('.xx' in s7) or ('.xx' in s8) or ('.xx' in s9) or ('.xx' in s10) or ('.xx' in s11) or ('.xx' in s12) or ('.xx' in s13) or ('.xx' in s14):
    f = True
if f:
    print('YES')
else:
    print('NO')
