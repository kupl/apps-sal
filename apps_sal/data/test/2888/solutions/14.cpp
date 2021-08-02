#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define inf 100000000000000
typedef long long ll;
#define mp make_pair
#define f first 
#define s second
int n;
ll en[5005];
ll sen[5005];
ll dp[5005][5005];
ll power(ll x,ll y){
    ll res=1;
    while (y){
        if (y & 1){
            res=res*x; 
        }
        x=x*x;
        y=y>>1;
    }
    return res;
}
ll train(ll x){
    ll res=x;
    ll sum=0;
    while(x!=0){
        sum+=(x%10);
        x=x/10;
    }
    res+=power(sum,3);
    return res;
}
ll max_exp(int i,int j){
    //cout<<i<<" "<<j<<"\n";
    if(j>i || j<0){
        return 0;
    }
    if(i<0){
        return 0;
    }
    if(dp[i][j]!=-1){
        return dp[i][j];
    }
    ll maxi=0;
    maxi=max_exp(i-1,j-1);
    maxi=max(maxi,sen[j]*en[i]+max_exp(i-1,j));
    dp[i][j]=maxi;
    return dp[i][j];
}
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	ll stren;
	memset(dp,-1,sizeof(dp));
	cin>>n>>stren;
	for(int i=0;i<n;i++){
	    cin>>en[i];
	}
	sen[0]=stren;
	for(int i=1;i<n;i++){ 
	    sen[i]=train(sen[i-1]);
	}
	ll maxi=0;
	for(int i=0;i<n;i++){
	    //cout<<i<<" ";
	    maxi=max(maxi,max_exp(n-1,i));
	}
	cout<<maxi<<"\n";
	return 0;
}
