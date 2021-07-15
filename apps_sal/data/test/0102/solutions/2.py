n = int(input())
d = {}
d[0] = 'zero'
d[1] = 'one'
d[2] = 'two'
d[3] = 'three'
d[4] = 'four'
d[5] = 'five'
d[6] = 'six'
d[7] = 'seven'
d[8] = 'eight'
d[9] = 'nine'
d[10] = 'ten'
d[11] = 'eleven'
d[12] = 'twelve'
d[13] = 'thirteen'
d[14] = 'fourteen'
d[15] = 'fifteen'
d[16] = 'sixteen'
d[17] = 'seventeen'
d[18] = 'eighteen'
d[19] = 'nineteen'
d[20] = 'twenty'
d[30] = 'thirty'
d[40] = 'forty'
d[50] = 'fifty'
d[60] = 'sixty'
d[70] = 'seventy'
d[80] = 'eighty'
d[90] = 'ninety'
if n <= 19 or n % 10 == 0:
    print(d[n])
else:
    print(d[n - (n % 10)],'-',d[n % 10], sep = '')
    
