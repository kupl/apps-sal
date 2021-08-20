s = 'H,HE,LI,BE,B,C,N,O,F,NE,NA,MG,AL,SI,P,S,CL,AR,K,CA,SC,TI,V,CR,MN,FE,CO,NI,CU,ZN,GA,GE,AS,SE,BR,KR,RB,SR,Y,ZR,NB,MO,TC,RU,RH,PD,AG,CD,IN,SN,SB,TE,I,XE,CS,BA,LA,CE,PR,ND,PM,SM,EU,GD,TB,DY,HO,ER,TM,YB,LU,HF,TA,W,RE,OS,IR,PT,AU,HG,TL,PB,BI,PO,AT,RN,FR,RA,AC,TH,PA,U,NP,PU,AM,CM,BK,CF,ES,FM,MD,NO,LR,RF,DB,SG,BH,HS,MT,DS,RG,CN,NH,FL,MC,LV,TS,OG'.split(',')
x = input()
(count1, count2) = (1, 0)
for i in range(len(x)):
    (count1, count2) = (x[i] in s and count1 or (x[i - 1:i + 1] in s and count2), count1)
print(['NO', 'YES'][count1])
