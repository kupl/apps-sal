class Odd:
    def __init__(self,s:str):
        self.s=s

    def odd_str(self):
        m=[]
        l=int(len(self.s))
        for i in range(0,l,2):
            m.append(self.s[i])
        print(''.join(m))

odd1=Odd(input())
odd1.odd_str()
