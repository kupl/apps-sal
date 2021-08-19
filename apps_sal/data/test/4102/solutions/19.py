print(['No', 'Yes'][(lambda x: min([x[i] + x[::-1][i] in ['33', '46', '59', '77', '80', '64', '95', '08'] for i in range(len(x))]))(input())])
